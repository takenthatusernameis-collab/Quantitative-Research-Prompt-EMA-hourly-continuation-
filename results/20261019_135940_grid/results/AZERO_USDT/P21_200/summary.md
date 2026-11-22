# EMA Hourly Continuation — AZERO/USDT P21_200

**Symbol:** AZERO/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 227 |
| net_profit_factor | 0.8416 |
| net_win_rate | 0.5198 |
| gross_profit_factor | 1.1175 |
| gross_win_rate | 0.5286 |
| sharpe_ratio | -0.7534 |
| sortino_ratio | -0.1620 |
| max_drawdown | 0.2600 |
| cagr | -0.0742 |
| net_avg_win | 79.5262 |
| net_avg_loss | -102.3018 |
| avg_hold_time_bars | 70.0132 |
| exposure | 0.7192 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
