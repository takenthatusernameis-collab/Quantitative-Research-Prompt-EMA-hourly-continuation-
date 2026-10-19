# EMA Hourly Continuation — LDO/USDT P21_89

**Symbol:** LDO/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 745 |
| net_profit_factor | 0.5335 |
| net_win_rate | 0.4336 |
| gross_profit_factor | 0.7713 |
| gross_win_rate | 0.4403 |
| sharpe_ratio | -5.4328 |
| sortino_ratio | -2.0867 |
| max_drawdown | 0.9201 |
| cagr | -0.6291 |
| net_avg_win | 32.4705 |
| net_avg_loss | -46.5867 |
| avg_hold_time_bars | 10.9638 |
| exposure | 0.3713 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
