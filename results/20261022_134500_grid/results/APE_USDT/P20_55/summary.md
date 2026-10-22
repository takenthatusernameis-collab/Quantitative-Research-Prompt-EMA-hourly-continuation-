# EMA Hourly Continuation — APE/USDT P20_55

**Symbol:** APE/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1000 |
| net_profit_factor | 0.5149 |
| net_win_rate | 0.4660 |
| gross_profit_factor | 0.8871 |
| gross_win_rate | 0.4810 |
| sharpe_ratio | -6.4528 |
| sortino_ratio | -2.8610 |
| max_drawdown | 0.9720 |
| cagr | -0.7535 |
| net_avg_win | 22.0983 |
| net_avg_loss | -37.4545 |
| avg_hold_time_bars | 4.6170 |
| exposure | 0.2099 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
