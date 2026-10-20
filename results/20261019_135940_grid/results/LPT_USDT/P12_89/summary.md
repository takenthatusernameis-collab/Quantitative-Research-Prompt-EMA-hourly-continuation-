# EMA Hourly Continuation — LPT/USDT P12_89

**Symbol:** LPT/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 675 |
| net_profit_factor | 0.6227 |
| net_win_rate | 0.4504 |
| gross_profit_factor | 0.8683 |
| gross_win_rate | 0.4548 |
| sharpe_ratio | -4.3483 |
| sortino_ratio | -1.5867 |
| max_drawdown | 0.8570 |
| cagr | -0.5300 |
| net_avg_win | 46.1360 |
| net_avg_loss | -60.7120 |
| avg_hold_time_bars | 18.9674 |
| exposure | 0.5820 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
