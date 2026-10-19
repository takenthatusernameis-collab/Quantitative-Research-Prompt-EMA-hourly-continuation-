# EMA Hourly Continuation — STX/USDT P89_100

**Symbol:** STX/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 585 |
| net_profit_factor | 0.3232 |
| net_win_rate | 0.4085 |
| gross_profit_factor | 0.7927 |
| gross_win_rate | 0.4410 |
| sharpe_ratio | -8.4634 |
| sortino_ratio | -2.9436 |
| max_drawdown | 0.9782 |
| cagr | -0.7791 |
| net_avg_win | 19.5373 |
| net_avg_loss | -41.7563 |
| avg_hold_time_bars | 1.9453 |
| exposure | 0.0515 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
