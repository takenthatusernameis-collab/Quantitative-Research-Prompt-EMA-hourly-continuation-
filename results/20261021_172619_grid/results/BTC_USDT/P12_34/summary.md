# EMA Hourly Continuation — BTC/USDT P12_34

**Symbol:** BTC/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 577 |
| net_profit_factor | 0.5372 |
| net_win_rate | 0.4887 |
| gross_profit_factor | 0.9842 |
| gross_win_rate | 0.5061 |
| sharpe_ratio | -4.2745 |
| sortino_ratio | -1.3909 |
| max_drawdown | 0.8378 |
| cagr | -0.4709 |
| net_avg_win | 34.4720 |
| net_avg_loss | -61.3400 |
| avg_hold_time_bars | 8.7695 |
| exposure | 0.2024 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
