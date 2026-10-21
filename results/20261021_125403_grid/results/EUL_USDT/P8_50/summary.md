# EMA Hourly Continuation — EUL/USDT P8_50

**Symbol:** EUL/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 670 |
| net_profit_factor | 0.7437 |
| net_win_rate | 0.4866 |
| gross_profit_factor | 0.9211 |
| gross_win_rate | 0.4866 |
| sharpe_ratio | -2.1763 |
| sortino_ratio | -0.8042 |
| max_drawdown | 0.6321 |
| cagr | -0.3094 |
| net_avg_win | 53.8780 |
| net_avg_loss | -68.6541 |
| avg_hold_time_bars | 14.7716 |
| exposure | 0.4499 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
