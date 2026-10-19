# EMA Hourly Continuation — NEAR/USDT P12_89

**Symbol:** NEAR/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 659 |
| net_profit_factor | 0.6367 |
| net_win_rate | 0.4643 |
| gross_profit_factor | 0.9088 |
| gross_win_rate | 0.4734 |
| sharpe_ratio | -3.9495 |
| sortino_ratio | -1.4238 |
| max_drawdown | 0.8241 |
| cagr | -0.4942 |
| net_avg_win | 46.9278 |
| net_avg_loss | -63.8947 |
| avg_hold_time_bars | 18.8968 |
| exposure | 0.5660 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
