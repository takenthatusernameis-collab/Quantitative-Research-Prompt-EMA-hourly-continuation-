# EMA Hourly Continuation — DIA/USDT P12_50

**Symbol:** DIA/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 680 |
| net_profit_factor | 0.6522 |
| net_win_rate | 0.4618 |
| gross_profit_factor | 0.8472 |
| gross_win_rate | 0.4618 |
| sharpe_ratio | -3.4748 |
| sortino_ratio | -1.2865 |
| max_drawdown | 0.7878 |
| cagr | -0.4463 |
| net_avg_win | 46.2850 |
| net_avg_loss | -60.8811 |
| avg_hold_time_bars | 9.9456 |
| exposure | 0.3060 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
