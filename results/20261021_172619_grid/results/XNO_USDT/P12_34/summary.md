# EMA Hourly Continuation — XNO/USDT P12_34

**Symbol:** XNO/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 599 |
| net_profit_factor | 0.5930 |
| net_win_rate | 0.4174 |
| gross_profit_factor | 0.7994 |
| gross_win_rate | 0.4174 |
| sharpe_ratio | -4.7956 |
| sortino_ratio | -1.6655 |
| max_drawdown | 0.8625 |
| cagr | -0.5364 |
| net_avg_win | 49.8273 |
| net_avg_loss | -60.1889 |
| avg_hold_time_bars | 6.5376 |
| exposure | 0.1780 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
