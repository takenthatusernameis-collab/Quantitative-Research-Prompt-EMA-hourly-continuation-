# EMA Hourly Continuation — ARB/USDT P12_200

**Symbol:** ARB/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 204 |
| net_profit_factor | 1.0117 |
| net_win_rate | 0.5392 |
| gross_profit_factor | 1.1573 |
| gross_win_rate | 0.5392 |
| sharpe_ratio | 0.0963 |
| sortino_ratio | 0.0199 |
| max_drawdown | 0.1311 |
| cagr | 0.0046 |
| net_avg_win | 91.8706 |
| net_avg_loss | -106.2675 |
| avg_hold_time_bars | 86.2745 |
| exposure | 0.8000 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
