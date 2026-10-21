# EMA Hourly Continuation — ADA/USDT P20_144

**Symbol:** ADA/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.8850 |
| net_win_rate | 0.5257 |
| gross_profit_factor | 1.0939 |
| gross_win_rate | 0.5257 |
| sharpe_ratio | -0.6725 |
| sortino_ratio | -0.1810 |
| max_drawdown | 0.2796 |
| cagr | -0.0828 |
| net_avg_win | 81.5708 |
| net_avg_loss | -102.1661 |
| avg_hold_time_bars | 33.5886 |
| exposure | 0.5344 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
