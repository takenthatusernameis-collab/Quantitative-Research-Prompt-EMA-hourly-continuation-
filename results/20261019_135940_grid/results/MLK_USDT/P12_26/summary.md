# EMA Hourly Continuation — MLK/USDT P12_26

**Symbol:** MLK/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1698 |
| net_profit_factor | 0.1851 |
| net_win_rate | 0.2415 |
| gross_profit_factor | 0.5305 |
| gross_win_rate | 0.2621 |
| sharpe_ratio | -21.3991 |
| sortino_ratio | -12.9092 |
| max_drawdown | 1.0000 |
| cagr | -0.9989 |
| net_avg_win | 5.5398 |
| net_avg_loss | -9.5274 |
| avg_hold_time_bars | 2.9482 |
| exposure | 0.2265 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
