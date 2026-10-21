# EMA Hourly Continuation — ZIL/USDT P34_100

**Symbol:** ZIL/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.7035 |
| net_win_rate | 0.4831 |
| gross_profit_factor | 0.9390 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -2.4064 |
| sortino_ratio | -0.7239 |
| max_drawdown | 0.6266 |
| cagr | -0.2830 |
| net_avg_win | 62.7874 |
| net_avg_loss | -83.4049 |
| avg_hold_time_bars | 11.5305 |
| exposure | 0.2322 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
