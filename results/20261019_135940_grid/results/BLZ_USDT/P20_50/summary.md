# EMA Hourly Continuation — BLZ/USDT P20_50

**Symbol:** BLZ/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1059 |
| net_profit_factor | 0.4720 |
| net_win_rate | 0.4089 |
| gross_profit_factor | 0.8347 |
| gross_win_rate | 0.4259 |
| sharpe_ratio | -8.8885 |
| sortino_ratio | -4.0817 |
| max_drawdown | 0.9932 |
| cagr | -0.8618 |
| net_avg_win | 20.5028 |
| net_avg_loss | -30.0476 |
| avg_hold_time_bars | 5.3711 |
| exposure | 0.2574 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
