# EMA Hourly Continuation — ARKM/USDT P8_12

**Symbol:** ARKM/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 251 |
| net_profit_factor | 0.7517 |
| net_win_rate | 0.5139 |
| gross_profit_factor | 1.0271 |
| gross_win_rate | 0.5139 |
| sharpe_ratio | -1.2866 |
| sortino_ratio | -0.2935 |
| max_drawdown | 0.3057 |
| cagr | -0.1256 |
| net_avg_win | 67.1556 |
| net_avg_loss | -94.4670 |
| avg_hold_time_bars | 4.5976 |
| exposure | 0.0525 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
