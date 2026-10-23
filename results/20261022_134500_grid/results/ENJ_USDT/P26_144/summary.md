# EMA Hourly Continuation — ENJ/USDT P26_144

**Symbol:** ENJ/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 488 |
| net_profit_factor | 0.6964 |
| net_win_rate | 0.4939 |
| gross_profit_factor | 1.0049 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.6003 |
| sortino_ratio | -0.8062 |
| max_drawdown | 0.6586 |
| cagr | -0.3204 |
| net_avg_win | 59.2507 |
| net_avg_loss | -83.0157 |
| avg_hold_time_bars | 22.8238 |
| exposure | 0.5040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
