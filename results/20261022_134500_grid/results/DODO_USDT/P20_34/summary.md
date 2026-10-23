# EMA Hourly Continuation — DODO/USDT P20_34

**Symbol:** DODO/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1196 |
| net_profit_factor | 0.3858 |
| net_win_rate | 0.4089 |
| gross_profit_factor | 0.8338 |
| gross_win_rate | 0.4406 |
| sharpe_ratio | -10.4610 |
| sortino_ratio | -5.1404 |
| max_drawdown | 0.9984 |
| cagr | -0.9215 |
| net_avg_win | 12.8220 |
| net_avg_loss | -22.9896 |
| avg_hold_time_bars | 3.2517 |
| exposure | 0.1760 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
