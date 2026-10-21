# EMA Hourly Continuation — DUSK/USDT P12_50

**Symbol:** DUSK/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 674 |
| net_profit_factor | 0.7798 |
| net_win_rate | 0.4822 |
| gross_profit_factor | 0.9729 |
| gross_win_rate | 0.4822 |
| sharpe_ratio | -2.3897 |
| sortino_ratio | -0.8850 |
| max_drawdown | 0.6920 |
| cagr | -0.3352 |
| net_avg_win | 69.8710 |
| net_avg_loss | -83.4402 |
| avg_hold_time_bars | 10.7255 |
| exposure | 0.3286 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
