# EMA Hourly Continuation — ILV/USDT P50_200

**Symbol:** ILV/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 274 |
| net_profit_factor | 1.0001 |
| net_win_rate | 0.5511 |
| gross_profit_factor | 1.2205 |
| gross_win_rate | 0.5511 |
| sharpe_ratio | 0.0526 |
| sortino_ratio | 0.0126 |
| max_drawdown | 0.1095 |
| cagr | 0.0000 |
| net_avg_win | 91.7474 |
| net_avg_loss | -112.6250 |
| avg_hold_time_bars | 33.6971 |
| exposure | 0.4197 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
