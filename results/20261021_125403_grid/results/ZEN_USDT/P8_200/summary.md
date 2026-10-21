# EMA Hourly Continuation — ZEN/USDT P8_200

**Symbol:** ZEN/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 119 |
| net_profit_factor | 1.2569 |
| net_win_rate | 0.5798 |
| gross_profit_factor | 1.3999 |
| gross_win_rate | 0.5798 |
| sharpe_ratio | 0.7759 |
| sortino_ratio | 0.1247 |
| max_drawdown | 0.0964 |
| cagr | 0.0522 |
| net_avg_win | 96.6560 |
| net_avg_loss | -106.1196 |
| avg_hold_time_bars | 168.2269 |
| exposure | 0.9100 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
