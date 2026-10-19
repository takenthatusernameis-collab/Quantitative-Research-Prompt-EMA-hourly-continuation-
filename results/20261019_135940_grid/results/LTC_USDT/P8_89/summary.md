# EMA Hourly Continuation — LTC/USDT P8_89

**Symbol:** LTC/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 750 |
| net_profit_factor | 0.4957 |
| net_win_rate | 0.4520 |
| gross_profit_factor | 0.9279 |
| gross_win_rate | 0.4680 |
| sharpe_ratio | -6.4626 |
| sortino_ratio | -2.4659 |
| max_drawdown | 0.9569 |
| cagr | -0.7129 |
| net_avg_win | 27.7349 |
| net_avg_loss | -46.1480 |
| avg_hold_time_bars | 18.5467 |
| exposure | 0.6323 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
