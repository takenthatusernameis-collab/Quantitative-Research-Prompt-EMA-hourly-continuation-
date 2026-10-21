# EMA Hourly Continuation — BDX/USDT P12_34

**Symbol:** BDX/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.3947 |
| net_win_rate | 0.3785 |
| gross_profit_factor | 0.6517 |
| gross_win_rate | 0.3814 |
| sharpe_ratio | -5.6647 |
| sortino_ratio | -1.5314 |
| max_drawdown | 0.8391 |
| cagr | -0.5154 |
| net_avg_win | 40.7795 |
| net_avg_loss | -62.9224 |
| avg_hold_time_bars | 5.5819 |
| exposure | 0.0898 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
