# EMA Hourly Continuation — BTT/USDT P8_34

**Symbol:** BTT/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1416 |
| net_profit_factor | 0.2776 |
| net_win_rate | 0.3439 |
| gross_profit_factor | 0.6477 |
| gross_win_rate | 0.3969 |
| sharpe_ratio | -16.2749 |
| sortino_ratio | -8.8844 |
| max_drawdown | 1.0000 |
| cagr | -0.9919 |
| net_avg_win | 7.8913 |
| net_avg_loss | -14.9010 |
| avg_hold_time_bars | 5.8948 |
| exposure | 0.3794 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
