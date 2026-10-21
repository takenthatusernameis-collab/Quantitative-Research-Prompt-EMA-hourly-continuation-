# EMA Hourly Continuation — TRX/USDT P55_89

**Symbol:** TRX/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 242 |
| net_profit_factor | 0.3911 |
| net_win_rate | 0.4752 |
| gross_profit_factor | 0.9902 |
| gross_win_rate | 0.5041 |
| sharpe_ratio | -4.2350 |
| sortino_ratio | -0.9735 |
| max_drawdown | 0.6749 |
| cagr | -0.3591 |
| net_avg_win | 37.5861 |
| net_avg_loss | -87.0133 |
| avg_hold_time_bars | 8.2975 |
| exposure | 0.0913 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
