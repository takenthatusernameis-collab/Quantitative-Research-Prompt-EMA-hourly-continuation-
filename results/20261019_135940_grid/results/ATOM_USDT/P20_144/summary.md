# EMA Hourly Continuation — ATOM/USDT P20_144

**Symbol:** ATOM/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 463 |
| net_profit_factor | 0.6901 |
| net_win_rate | 0.5011 |
| gross_profit_factor | 1.0252 |
| gross_win_rate | 0.5119 |
| sharpe_ratio | -2.3174 |
| sortino_ratio | -0.7064 |
| max_drawdown | 0.5943 |
| cagr | -0.2835 |
| net_avg_win | 54.4215 |
| net_avg_loss | -79.2057 |
| avg_hold_time_bars | 25.7171 |
| exposure | 0.5412 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
