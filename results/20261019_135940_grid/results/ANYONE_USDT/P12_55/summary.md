# EMA Hourly Continuation — ANYONE/USDT P12_55

**Symbol:** ANYONE/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 888 |
| net_profit_factor | 0.6190 |
| net_win_rate | 0.4437 |
| gross_profit_factor | 0.8173 |
| gross_win_rate | 0.4448 |
| sharpe_ratio | -5.1327 |
| sortino_ratio | -2.2670 |
| max_drawdown | 0.9142 |
| cagr | -0.6586 |
| net_avg_win | 37.5958 |
| net_avg_loss | -48.4417 |
| avg_hold_time_bars | 8.3187 |
| exposure | 0.3733 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
