# EMA Hourly Continuation — STX/USDT P8_20

**Symbol:** STX/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 547 |
| net_profit_factor | 0.7384 |
| net_win_rate | 0.5082 |
| gross_profit_factor | 1.0024 |
| gross_win_rate | 0.5082 |
| sharpe_ratio | -2.0568 |
| sortino_ratio | -0.6904 |
| max_drawdown | 0.5955 |
| cagr | -0.2711 |
| net_avg_win | 55.8106 |
| net_avg_loss | -78.1082 |
| avg_hold_time_bars | 5.3912 |
| exposure | 0.1334 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
