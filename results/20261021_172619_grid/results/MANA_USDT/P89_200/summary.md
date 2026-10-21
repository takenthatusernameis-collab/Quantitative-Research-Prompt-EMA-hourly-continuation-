# EMA Hourly Continuation — MANA/USDT P89_200

**Symbol:** MANA/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 286 |
| net_profit_factor | 0.7147 |
| net_win_rate | 0.4860 |
| gross_profit_factor | 0.9284 |
| gross_win_rate | 0.4860 |
| sharpe_ratio | -1.6974 |
| sortino_ratio | -0.4103 |
| max_drawdown | 0.3946 |
| cagr | -0.1721 |
| net_avg_win | 68.0636 |
| net_avg_loss | -90.0495 |
| avg_hold_time_bars | 15.9476 |
| exposure | 0.2073 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
