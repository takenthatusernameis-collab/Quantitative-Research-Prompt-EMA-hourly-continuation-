# EMA Hourly Continuation — BCH/USDT P8_89

**Symbol:** BCH/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 477 |
| net_profit_factor | 0.7684 |
| net_win_rate | 0.4948 |
| gross_profit_factor | 1.0002 |
| gross_win_rate | 0.4948 |
| sharpe_ratio | -1.9711 |
| sortino_ratio | -0.6160 |
| max_drawdown | 0.5590 |
| cagr | -0.2463 |
| net_avg_win | 71.4703 |
| net_avg_loss | -91.0850 |
| avg_hold_time_bars | 27.7254 |
| exposure | 0.6011 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
