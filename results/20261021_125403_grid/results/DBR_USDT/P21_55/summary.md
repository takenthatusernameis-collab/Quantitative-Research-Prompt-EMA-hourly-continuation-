# EMA Hourly Continuation — DBR/USDT P21_55

**Symbol:** DBR/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 402 |
| net_profit_factor | 0.6169 |
| net_win_rate | 0.4627 |
| gross_profit_factor | 0.8989 |
| gross_win_rate | 0.4652 |
| sharpe_ratio | -3.6937 |
| sortino_ratio | -1.1825 |
| max_drawdown | 0.6797 |
| cagr | -0.4195 |
| net_avg_win | 57.5087 |
| net_avg_loss | -80.2779 |
| avg_hold_time_bars | 10.7910 |
| exposure | 0.2467 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
