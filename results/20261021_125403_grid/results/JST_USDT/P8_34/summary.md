# EMA Hourly Continuation — JST/USDT P8_34

**Symbol:** JST/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 735 |
| net_profit_factor | 0.5737 |
| net_win_rate | 0.5034 |
| gross_profit_factor | 1.0653 |
| gross_win_rate | 0.5143 |
| sharpe_ratio | -4.4703 |
| sortino_ratio | -1.7362 |
| max_drawdown | 0.8706 |
| cagr | -0.5499 |
| net_avg_win | 31.5124 |
| net_avg_loss | -55.6846 |
| avg_hold_time_bars | 9.4898 |
| exposure | 0.3156 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
