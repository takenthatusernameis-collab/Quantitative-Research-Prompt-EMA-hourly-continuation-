# EMA Hourly Continuation — LSK/USDT P8_21

**Symbol:** LSK/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1272 |
| net_profit_factor | 0.4747 |
| net_win_rate | 0.4458 |
| gross_profit_factor | 1.0382 |
| gross_win_rate | 0.4741 |
| sharpe_ratio | -9.2045 |
| sortino_ratio | -4.6255 |
| max_drawdown | 0.9971 |
| cagr | -0.9002 |
| net_avg_win | 15.8910 |
| net_avg_loss | -26.9213 |
| avg_hold_time_bars | 4.3829 |
| exposure | 0.2534 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
