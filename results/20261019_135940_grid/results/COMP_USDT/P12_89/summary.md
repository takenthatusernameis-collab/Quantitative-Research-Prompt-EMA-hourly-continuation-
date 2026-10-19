# EMA Hourly Continuation — COMP/USDT P12_89

**Symbol:** COMP/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 675 |
| net_profit_factor | 0.6537 |
| net_win_rate | 0.5052 |
| gross_profit_factor | 1.0179 |
| gross_win_rate | 0.5185 |
| sharpe_ratio | -3.0517 |
| sortino_ratio | -1.1215 |
| max_drawdown | 0.7555 |
| cagr | -0.4120 |
| net_avg_win | 40.7661 |
| net_avg_loss | -63.6709 |
| avg_hold_time_bars | 19.6311 |
| exposure | 0.6023 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
