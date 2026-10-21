# EMA Hourly Continuation — GMX/USDT P21_144

**Symbol:** GMX/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.6961 |
| net_win_rate | 0.4631 |
| gross_profit_factor | 0.8688 |
| gross_win_rate | 0.4631 |
| sharpe_ratio | -2.6363 |
| sortino_ratio | -0.8368 |
| max_drawdown | 0.6402 |
| cagr | -0.3206 |
| net_avg_win | 61.3313 |
| net_avg_loss | -75.9899 |
| avg_hold_time_bars | 21.1796 |
| exposure | 0.4823 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
