# EMA Hourly Continuation — BSV/USDT P8_55

**Symbol:** BSV/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1166 |
| net_profit_factor | 0.4703 |
| net_win_rate | 0.4262 |
| gross_profit_factor | 0.8383 |
| gross_win_rate | 0.4434 |
| sharpe_ratio | -8.4557 |
| sortino_ratio | -4.0570 |
| max_drawdown | 0.9934 |
| cagr | -0.8625 |
| net_avg_win | 17.7437 |
| net_avg_loss | -28.0271 |
| avg_hold_time_bars | 9.0918 |
| exposure | 0.4819 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
