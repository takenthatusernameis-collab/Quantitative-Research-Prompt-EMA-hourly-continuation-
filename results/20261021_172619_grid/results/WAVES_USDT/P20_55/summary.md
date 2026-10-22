# EMA Hourly Continuation — WAVES/USDT P20_55

**Symbol:** WAVES/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 552 |
| net_profit_factor | 0.5485 |
| net_win_rate | 0.4239 |
| gross_profit_factor | 0.7676 |
| gross_win_rate | 0.4239 |
| sharpe_ratio | -4.8672 |
| sortino_ratio | -1.6265 |
| max_drawdown | 0.8535 |
| cagr | -0.5305 |
| net_avg_win | 44.1505 |
| net_avg_loss | -59.2262 |
| avg_hold_time_bars | 8.1232 |
| exposure | 0.2038 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
