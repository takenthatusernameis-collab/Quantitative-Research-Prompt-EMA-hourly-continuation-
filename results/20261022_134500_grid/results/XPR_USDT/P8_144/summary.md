# EMA Hourly Continuation — XPR/USDT P8_144

**Symbol:** XPR/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 620 |
| net_profit_factor | 0.5662 |
| net_win_rate | 0.4758 |
| gross_profit_factor | 0.8687 |
| gross_win_rate | 0.4790 |
| sharpe_ratio | -3.9836 |
| sortino_ratio | -1.3896 |
| max_drawdown | 0.8308 |
| cagr | -0.4903 |
| net_avg_win | 36.0945 |
| net_avg_loss | -57.8671 |
| avg_hold_time_bars | 24.0177 |
| exposure | 0.6769 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
