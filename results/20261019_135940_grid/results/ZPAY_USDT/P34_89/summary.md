# EMA Hourly Continuation — ZPAY/USDT P34_89

**Symbol:** ZPAY/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 640 |
| net_profit_factor | 0.4402 |
| net_win_rate | 0.3359 |
| gross_profit_factor | 0.6177 |
| gross_win_rate | 0.3406 |
| sharpe_ratio | -7.2902 |
| sortino_ratio | -2.5645 |
| max_drawdown | 0.9580 |
| cagr | -0.7092 |
| net_avg_win | 34.9462 |
| net_avg_loss | -40.1643 |
| avg_hold_time_bars | 12.1797 |
| exposure | 0.3527 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
