# EMA Hourly Continuation — ZEC/USDT P26_100

**Symbol:** ZEC/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 390 |
| net_profit_factor | 1.0241 |
| net_win_rate | 0.5538 |
| gross_profit_factor | 1.2260 |
| gross_win_rate | 0.5538 |
| sharpe_ratio | 0.2205 |
| sortino_ratio | 0.0633 |
| max_drawdown | 0.2876 |
| cagr | 0.0199 |
| net_avg_win | 99.6568 |
| net_avg_loss | -120.8020 |
| avg_hold_time_bars | 18.3000 |
| exposure | 0.3244 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
