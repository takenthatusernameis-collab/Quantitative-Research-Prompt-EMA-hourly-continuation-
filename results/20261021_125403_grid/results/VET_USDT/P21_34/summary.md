# EMA Hourly Continuation — VET/USDT P21_34

**Symbol:** VET/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 302 |
| net_profit_factor | 0.6896 |
| net_win_rate | 0.5033 |
| gross_profit_factor | 1.0094 |
| gross_win_rate | 0.5033 |
| sharpe_ratio | -1.9964 |
| sortino_ratio | -0.4994 |
| max_drawdown | 0.4534 |
| cagr | -0.2032 |
| net_avg_win | 63.5552 |
| net_avg_loss | -93.3899 |
| avg_hold_time_bars | 5.2119 |
| exposure | 0.0715 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
