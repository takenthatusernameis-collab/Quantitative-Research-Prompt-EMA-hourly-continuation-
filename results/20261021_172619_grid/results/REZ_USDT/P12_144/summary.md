# EMA Hourly Continuation — REZ/USDT P12_144

**Symbol:** REZ/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 394 |
| net_profit_factor | 0.9716 |
| net_win_rate | 0.5305 |
| gross_profit_factor | 1.1206 |
| gross_win_rate | 0.5305 |
| sharpe_ratio | -0.1365 |
| sortino_ratio | -0.0394 |
| max_drawdown | 0.2240 |
| cagr | -0.0250 |
| net_avg_win | 99.1623 |
| net_avg_loss | -115.3064 |
| avg_hold_time_bars | 35.7640 |
| exposure | 0.6501 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
