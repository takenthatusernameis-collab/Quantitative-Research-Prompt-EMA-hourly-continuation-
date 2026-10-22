# EMA Hourly Continuation — LDO/USDT P34_89

**Symbol:** LDO/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 702 |
| net_profit_factor | 0.5282 |
| net_win_rate | 0.4430 |
| gross_profit_factor | 0.7999 |
| gross_win_rate | 0.4558 |
| sharpe_ratio | -5.1784 |
| sortino_ratio | -1.9309 |
| max_drawdown | 0.9026 |
| cagr | -0.6031 |
| net_avg_win | 32.4629 |
| net_avg_loss | -48.8838 |
| avg_hold_time_bars | 7.8205 |
| exposure | 0.2495 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
