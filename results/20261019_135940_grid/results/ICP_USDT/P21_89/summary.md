# EMA Hourly Continuation — ICP/USDT P21_89

**Symbol:** ICP/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 758 |
| net_profit_factor | 0.5806 |
| net_win_rate | 0.4749 |
| gross_profit_factor | 0.9303 |
| gross_win_rate | 0.4815 |
| sharpe_ratio | -4.8288 |
| sortino_ratio | -1.8498 |
| max_drawdown | 0.9048 |
| cagr | -0.5983 |
| net_avg_win | 34.5626 |
| net_avg_loss | -53.8444 |
| avg_hold_time_bars | 10.7401 |
| exposure | 0.3700 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
