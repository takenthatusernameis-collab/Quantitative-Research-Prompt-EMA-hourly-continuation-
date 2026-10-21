# EMA Hourly Continuation — CRO/USDT P8_89

**Symbol:** CRO/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 508 |
| net_profit_factor | 0.7806 |
| net_win_rate | 0.5138 |
| gross_profit_factor | 1.0473 |
| gross_win_rate | 0.5138 |
| sharpe_ratio | -1.7060 |
| sortino_ratio | -0.5522 |
| max_drawdown | 0.4971 |
| cagr | -0.2246 |
| net_avg_win | 64.3521 |
| net_avg_loss | -87.1135 |
| avg_hold_time_bars | 27.0335 |
| exposure | 0.6242 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
