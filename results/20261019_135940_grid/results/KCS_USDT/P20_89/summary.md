# EMA Hourly Continuation — KCS/USDT P20_89

**Symbol:** KCS/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 688 |
| net_profit_factor | 0.2859 |
| net_win_rate | 0.3910 |
| gross_profit_factor | 0.7424 |
| gross_win_rate | 0.4302 |
| sharpe_ratio | -9.2605 |
| sortino_ratio | -3.4494 |
| max_drawdown | 0.9902 |
| cagr | -0.8392 |
| net_avg_win | 14.7326 |
| net_avg_loss | -33.0823 |
| avg_hold_time_bars | 12.6991 |
| exposure | 0.3971 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
