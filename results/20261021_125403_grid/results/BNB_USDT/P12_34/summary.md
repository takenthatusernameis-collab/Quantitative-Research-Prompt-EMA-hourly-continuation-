# EMA Hourly Continuation — BNB/USDT P12_34

**Symbol:** BNB/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 527 |
| net_profit_factor | 0.5489 |
| net_win_rate | 0.4934 |
| gross_profit_factor | 0.9692 |
| gross_win_rate | 0.4953 |
| sharpe_ratio | -4.2660 |
| sortino_ratio | -1.4158 |
| max_drawdown | 0.8133 |
| cagr | -0.4758 |
| net_avg_win | 37.5595 |
| net_avg_loss | -66.6323 |
| avg_hold_time_bars | 6.8273 |
| exposure | 0.1635 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
