# EMA Hourly Continuation — ZEC/USDT P21_144

**Symbol:** ZEC/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 475 |
| net_profit_factor | 0.8091 |
| net_win_rate | 0.5284 |
| gross_profit_factor | 1.1214 |
| gross_win_rate | 0.5305 |
| sharpe_ratio | -1.2936 |
| sortino_ratio | -0.4007 |
| max_drawdown | 0.4293 |
| cagr | -0.1741 |
| net_avg_win | 64.4085 |
| net_avg_loss | -89.2042 |
| avg_hold_time_bars | 24.1411 |
| exposure | 0.5212 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
