# EMA Hourly Continuation — LDO/USDT P20_89

**Symbol:** LDO/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 741 |
| net_profit_factor | 0.5344 |
| net_win_rate | 0.4345 |
| gross_profit_factor | 0.7705 |
| gross_win_rate | 0.4426 |
| sharpe_ratio | -5.3443 |
| sortino_ratio | -2.0479 |
| max_drawdown | 0.9163 |
| cagr | -0.6222 |
| net_avg_win | 32.5522 |
| net_avg_loss | -46.8119 |
| avg_hold_time_bars | 11.2200 |
| exposure | 0.3779 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
