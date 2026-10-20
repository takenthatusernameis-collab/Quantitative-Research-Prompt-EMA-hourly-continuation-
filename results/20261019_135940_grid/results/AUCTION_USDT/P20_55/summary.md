# EMA Hourly Continuation — AUCTION/USDT P20_55

**Symbol:** AUCTION/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 894 |
| net_profit_factor | 0.4873 |
| net_win_rate | 0.4273 |
| gross_profit_factor | 0.8439 |
| gross_win_rate | 0.4541 |
| sharpe_ratio | -7.6785 |
| sortino_ratio | -3.2304 |
| max_drawdown | 0.9825 |
| cagr | -0.7953 |
| net_avg_win | 24.4213 |
| net_avg_loss | -37.3945 |
| avg_hold_time_bars | 6.9955 |
| exposure | 0.2831 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
