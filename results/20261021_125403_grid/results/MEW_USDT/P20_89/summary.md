# EMA Hourly Continuation — MEW/USDT P20_89

**Symbol:** MEW/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.8150 |
| net_win_rate | 0.5021 |
| gross_profit_factor | 0.9939 |
| gross_win_rate | 0.5021 |
| sharpe_ratio | -1.3163 |
| sortino_ratio | -0.4097 |
| max_drawdown | 0.3861 |
| cagr | -0.1728 |
| net_avg_win | 70.4796 |
| net_avg_loss | -87.2102 |
| avg_hold_time_bars | 17.5487 |
| exposure | 0.3765 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
