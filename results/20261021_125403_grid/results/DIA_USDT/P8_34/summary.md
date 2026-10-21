# EMA Hourly Continuation — DIA/USDT P8_34

**Symbol:** DIA/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 794 |
| net_profit_factor | 0.7162 |
| net_win_rate | 0.4899 |
| gross_profit_factor | 0.9554 |
| gross_win_rate | 0.4899 |
| sharpe_ratio | -2.9838 |
| sortino_ratio | -1.2002 |
| max_drawdown | 0.7584 |
| cagr | -0.4232 |
| net_avg_win | 48.6739 |
| net_avg_loss | -65.2795 |
| avg_hold_time_bars | 8.7960 |
| exposure | 0.3160 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
