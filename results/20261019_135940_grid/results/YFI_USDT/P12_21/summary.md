# EMA Hourly Continuation — YFI/USDT P12_21

**Symbol:** YFI/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1569 |
| net_profit_factor | 0.1834 |
| net_win_rate | 0.3671 |
| gross_profit_factor | 0.7761 |
| gross_win_rate | 0.4359 |
| sharpe_ratio | -16.3550 |
| sortino_ratio | -9.3932 |
| max_drawdown | 1.0000 |
| cagr | -0.9927 |
| net_avg_win | 3.8979 |
| net_avg_loss | -12.3315 |
| avg_hold_time_bars | 2.6444 |
| exposure | 0.1877 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
