# EMA Hourly Continuation — ATOM/USDT P12_34

**Symbol:** ATOM/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1196 |
| net_profit_factor | 0.3943 |
| net_win_rate | 0.4515 |
| gross_profit_factor | 0.8492 |
| gross_win_rate | 0.4749 |
| sharpe_ratio | -8.6883 |
| sortino_ratio | -4.2649 |
| max_drawdown | 0.9949 |
| cagr | -0.8771 |
| net_avg_win | 11.9950 |
| net_avg_loss | -25.0390 |
| avg_hold_time_bars | 4.4724 |
| exposure | 0.2431 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
