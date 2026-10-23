# EMA Hourly Continuation — TRADE/USDT P12_89

**Symbol:** TRADE/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 623 |
| net_profit_factor | 0.6617 |
| net_win_rate | 0.4719 |
| gross_profit_factor | 0.9220 |
| gross_win_rate | 0.4767 |
| sharpe_ratio | -3.3450 |
| sortino_ratio | -1.1709 |
| max_drawdown | 0.7805 |
| cagr | -0.4331 |
| net_avg_win | 50.5210 |
| net_avg_loss | -68.2322 |
| avg_hold_time_bars | 18.0947 |
| exposure | 0.5124 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
